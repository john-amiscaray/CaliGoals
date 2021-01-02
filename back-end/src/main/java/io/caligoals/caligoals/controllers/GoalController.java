package io.caligoals.caligoals.controllers;

import io.caligoals.caligoals.dtos.GoalDto;
import io.caligoals.caligoals.dtos.Response;
import io.caligoals.caligoals.entities.Goal;
import io.caligoals.caligoals.entities.compositekeys.GoalId;
import io.caligoals.caligoals.services.GoalService;
import io.caligoals.caligoals.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
public class GoalController {

    @Autowired
    private GoalService goalService;
    @Autowired
    private UserService userService;

    @GetMapping("/user/{userId}/goal/{title}")
    public ResponseEntity<Response> getGoal(@PathVariable("userId") Long userId, @PathVariable("title") String title){

        GoalId goalId = new GoalId(userService.getUser(userId), title);
        Goal goal = goalService.getGoal(goalId);
        return new ResponseEntity<>(new Response(new GoalDto(goal)), HttpStatus.OK);

    }

    @PutMapping("/user/goal/edit")
    public ResponseEntity<Response> editGoal(@RequestBody GoalDto dto){

        goalService.editGoal(dto);
        return new ResponseEntity<>(new Response("Successfully edited goal"), HttpStatus.OK);

    }

    @PostMapping(value="/user/{userId}/goal/{title}/image", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<Response> setGoalImage(@PathVariable("userId") Long userId, @RequestParam MultipartFile
            file, @PathVariable("title") String title){

        GoalId goalId = new GoalId(userService.getUser(userId), title);
        goalService.setImage(goalId, file);
        return new ResponseEntity<>(new Response("Goal icon set successfully"), HttpStatus.OK);

    }
    @GetMapping("/user/{userId}/goal/{title}/image")
    public ResponseEntity<Object> getGoalImage(@PathVariable("userId") Long userId, @PathVariable("title") String title){

        Goal goal = goalService.getGoal(new GoalId(userService.getUser(userId), title));

        return ResponseEntity.ok()
                .contentType(MediaType.parseMediaType(MediaType.IMAGE_JPEG_VALUE))
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"Post " + goal.getGoalId().getTitle() + "\"")
                .body(goal.getGoalIcon());

    }

    @GetMapping("/user/{userId}/goals")
    public ResponseEntity<Response> getAllGoals(@PathVariable("userId") Long userId){

        return new ResponseEntity<>(new Response(goalService.getUserGoals(userId)), HttpStatus.OK);

    }

    @PostMapping("/user/{userId}/addGoal")
    public ResponseEntity<Response> addGoal(@PathVariable("userId") Long userId, @RequestBody GoalDto dto){

        if(dto.getUserId().equals(userId)) {
            goalService.addGoal(dto);
            return new ResponseEntity<>(new Response("Successfully added goal"), HttpStatus.OK);
        }else{

            return ResponseEntity.badRequest().build();

        }

    }

    @PutMapping("/user/{userId}/goal/{title}/addTime/{time}")
    public ResponseEntity<Response> addTimeToGoal(@PathVariable("userId") Long userId,
                                                  @PathVariable("title") String title,
                                                  @PathVariable("time") Long timesSpent){

        goalService.addTimeToGoal(title, userId, timesSpent);
        return new ResponseEntity<>(new Response("Successfully added time to goal"), HttpStatus.OK);

    }


}
