package io.caligoals.caligoals.data;

import io.caligoals.caligoals.entities.Goal;
import io.caligoals.caligoals.entities.User;
import io.caligoals.caligoals.entities.compositekeys.GoalId;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface GoalRepo extends JpaRepository<Goal, GoalId> {

    List<Goal> findAllByGoalId_User(User goalId_user);

}
