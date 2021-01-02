package io.caligoals.caligoals.controllers;

import io.caligoals.caligoals.dtos.CommentDto;
import io.caligoals.caligoals.dtos.Response;
import io.caligoals.caligoals.services.CommentService;
import io.caligoals.caligoals.services.PostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class CommentController {

    @Autowired
    private PostService postService;
    @Autowired
    private CommentService commentService;

    @GetMapping("/post/{postId}/comments")
    public ResponseEntity<Response> getAllCommentsOfPost(@PathVariable("postId") Long postId){

        return new ResponseEntity<>(new Response(postService.getComments(postId)), HttpStatus.OK);

    }

    @PostMapping("/post/add")
    public ResponseEntity<Response> addPost(@RequestBody CommentDto dto){

        this.commentService.addComment(dto);
        return new ResponseEntity<>(new Response("Successfully added comment"), HttpStatus.OK);

    }


}
