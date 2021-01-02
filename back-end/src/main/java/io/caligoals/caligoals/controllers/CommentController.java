package io.caligoals.caligoals.controllers;

import io.caligoals.caligoals.dtos.CommentDto;
import io.caligoals.caligoals.dtos.Response;
import io.caligoals.caligoals.services.CommentService;
import io.caligoals.caligoals.services.PostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.stream.Collectors;

@RestController
public class CommentController {

    @Autowired
    private PostService postService;
    @Autowired
    private CommentService commentService;

    @GetMapping("/post/{postId}/comments")
    public ResponseEntity<Response> getAllCommentsOfPost(@PathVariable("postId") Long postId){

        return new ResponseEntity<>(new Response(postService.getComments(postId).stream()
                .map(CommentDto::new)
                .collect(Collectors.toList())
        ), HttpStatus.OK);

    }

    @PostMapping("/user/{userId}/post/{postId}/comment")
    public ResponseEntity<Response> addComment(@RequestBody CommentDto dto, @PathVariable("userId") Long userId,
                                               @PathVariable("postId") Long postId){

        dto.setPostId(postId);
        dto.setUserId(userId);
        commentService.addComment(dto);
        return new ResponseEntity<>(new Response("Successfully added comment"), HttpStatus.OK);

    }


}
