package io.caligoals.caligoals.controllers;

import io.caligoals.caligoals.dtos.AppUserDetails;
import io.caligoals.caligoals.dtos.Response;
import io.caligoals.caligoals.dtos.UserDto;
import io.caligoals.caligoals.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AuthController {

    @Autowired
    private UserService userService;

    @PostMapping("/auth/signup")
    public ResponseEntity<Response> signUp(@RequestBody UserDto userDto){

        this.userService.saveUser(userDto);
        return new ResponseEntity<>(new Response("Successfully signed up"), HttpStatus.OK);

    }

    @PostMapping("/auth/login")
    public ResponseEntity<Response> login(){

        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        AppUserDetails details = (AppUserDetails) auth.getPrincipal();
        return new ResponseEntity<>(new Response(details.getId()), HttpStatus.OK);

    }


}
