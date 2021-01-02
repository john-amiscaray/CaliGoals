package io.caligoals.caligoals.controllers;

import io.caligoals.caligoals.dtos.Response;
import io.caligoals.caligoals.dtos.UserDto;
import io.caligoals.caligoals.entities.User;
import io.caligoals.caligoals.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;

@RestController
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/user/{userId}/profile-picture")
    public ResponseEntity<Object> getProfilePicture(@PathVariable("userId") Long userId){

        User user = userService.getUser(userId);
        return ResponseEntity.ok()
                .contentType(MediaType.parseMediaType(MediaType.IMAGE_PNG_VALUE))
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + user.getUsername() + "\"")
                .body(user.getProfilePicture());

    }

    @PostMapping(value="/user/{userId}/profile-picture", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<Response> setProfilePicture(@PathVariable("userId") Long userId, @RequestParam MultipartFile file) throws IOException {

        userService.setProfilePicture(userId, file);
        return new ResponseEntity<>(new Response("Profile picture set successfully"), HttpStatus.OK);

    }

    @GetMapping("/user/{userId}/add-friend/{friendId}")
    public ResponseEntity<Response> addFriend(@PathVariable("userId") Long userId, @PathVariable("friendId") Long friendId){

        if(userId.equals(friendId)) {
            return ResponseEntity.badRequest().build();
        }
        userService.addAsFriend(friendId, userId);
        return new ResponseEntity<>(new Response("Successfully added friend"), HttpStatus.OK);

    }

    @GetMapping("/user/{userId}/friends")
    public ResponseEntity<Response> getAllFriends(@PathVariable("userId") Long userId){

        List<UserDto> friends = userService.getFriends(userId);
        return new ResponseEntity<>(new Response(friends), HttpStatus.OK);

    }

    @GetMapping("/user/{userId}/growth")
    public ResponseEntity<Response> getGrowthAmount(@PathVariable("userId") Long userId){

        Long growth = userService.getGrowthAmount(userId);
        return new ResponseEntity<>(new Response(growth), HttpStatus.OK);

    }

    @PutMapping("/user/{userId}/addGrowth/{growthAmount}")
    public ResponseEntity<Response> addGrowth(@PathVariable("userId") Long userId, @PathVariable("growthAmount") Long growthAmount){

        userService.addToGrowthAmount(growthAmount, userId);
        return new ResponseEntity<>(new Response("Successfully grown cat"), HttpStatus.OK);

    }


}
