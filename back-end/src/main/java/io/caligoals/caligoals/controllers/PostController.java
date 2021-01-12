package io.caligoals.caligoals.controllers;

import io.caligoals.caligoals.dtos.PostDto;
import io.caligoals.caligoals.dtos.Response;
import io.caligoals.caligoals.entities.Post;
import io.caligoals.caligoals.entities.User;
import io.caligoals.caligoals.services.PostService;
import io.caligoals.caligoals.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.stream.Collectors;

@RestController
public class PostController {

    @Autowired
    private PostService postService;
    @Autowired
    private UserService userService;

    @PostMapping("/user/post")
    public ResponseEntity<Response> addPost(@RequestBody PostDto dto){

        dto.setUserId(userService.getLoggedInUser().getId());
        Post post = postService.addPost(dto);
        userService.addPost(post, userService.getLoggedInUser().getId());
        return new ResponseEntity<>(new Response(post.getPostId()), HttpStatus.OK);

    }

    @PostMapping(value="/user/post/{postId}/image", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<Response> setPostImage(@RequestParam MultipartFile
            file, @PathVariable("postId") Long postId) throws IOException, IllegalAccessException {

        postService.setImage(postId, file, userService.getLoggedInUser().getId());
        return new ResponseEntity<>(new Response("Post image set successfully"), HttpStatus.OK);

    }

    @GetMapping("/user/{userId}/post/{postId}/image")
    public ResponseEntity<Object> getPostImage(@PathVariable("postId") Long postId, @PathVariable("userId") Long userId){

        Post post = postService.getPost(postId);
        User user = userService.getUser(userId);
        if(user.getPosts().contains(post)) {
            return ResponseEntity.ok()
                    .contentType(MediaType.parseMediaType(MediaType.IMAGE_PNG_VALUE))
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"Post " + post.getPostId() + "\"")
                    .body(post.getImage());
        }else{

            return new ResponseEntity<>(new Response("Cannot find that post from that user"), HttpStatus.FORBIDDEN);

        }
    }

    @GetMapping("/user/{userId}/posts")
    public ResponseEntity<Response> getAllPosts(@PathVariable("userId") Long userId){

        User user = userService.getUser(userId);
        return new ResponseEntity<>(new Response(user.getPosts().stream()
                .map(PostDto::new)
                .collect(Collectors.toList())), HttpStatus.OK);

    }

    @GetMapping("/post/{postId}")
    public ResponseEntity<Response> getPost(@PathVariable("postId") Long postId){

        Post post = postService.getPost(postId);
        return new ResponseEntity<>(new Response(new PostDto(post)), HttpStatus.OK);

    }

    @GetMapping("/user/feed")
    public ResponseEntity<Response> getPostsOfUsersFriends(){

        return new ResponseEntity<>(new Response(postService.getFeed(userService.getLoggedInUser().getId())), HttpStatus.OK);

    }

}
