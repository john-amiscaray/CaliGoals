package io.caligoals.caligoals.services;

import io.caligoals.caligoals.data.GoalRepo;
import io.caligoals.caligoals.data.UserRepo;
import io.caligoals.caligoals.dtos.GoalDto;
import io.caligoals.caligoals.entities.Goal;
import io.caligoals.caligoals.entities.Post;
import io.caligoals.caligoals.entities.User;
import io.caligoals.caligoals.entities.compositekeys.GoalId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class GoalService {

    private final GoalRepo goalRepo;
    private final UserService userService;

    @Autowired
    public GoalService(GoalRepo goalRepo, UserService userService){

        this.goalRepo = goalRepo;
        this.userService = userService;

    }

    public Goal getGoal(GoalId goalId){

        return goalRepo.findById(goalId).orElseThrow();

    }

    public List<GoalDto> getUserGoals(Long userId){

        return goalRepo.findAllByGoalId_User(userService.getUser(userId)).stream()
                .map(GoalDto::new)
                .collect(Collectors.toList());

    }

    public void addGoal(GoalDto dto){

        Goal goal = new Goal(dto, userService);
        goalRepo.save(goal);

    }

    public void editGoal(GoalDto dto){

        Goal goal = new Goal(dto, userService);
        if (goalRepo.findById(goal.getGoalId()).isPresent()){

            goalRepo.save(goal);

        }else{

            throw new IllegalArgumentException("Goal does not exist");

        }

    }

    public void editGoal(Goal goal){

        if (goalRepo.findById(goal.getGoalId()).isPresent()){

            goalRepo.save(goal);

        }else{

            throw new IllegalArgumentException("Goal does not exist");

        }

    }

    public void setImage(GoalId goalId, MultipartFile file) {


        try {
            Goal goal = getGoal(goalId);
            goal.setGoalIcon(file.getBytes());
            editGoal(goal);
        } catch (IOException ex) {

            throw new IllegalArgumentException("You cannot edit this goal");

        }


    }

    public void addTimeToGoal(String title, Long userId, Long timeSpent){

        User user = userService.getUser(userId);
        GoalId id = new GoalId(user, title );
        Goal goal = getGoal(id);
        goal.setTimeSpent(goal.getTimeSpent() + timeSpent);
        editGoal(goal);

    }


}
