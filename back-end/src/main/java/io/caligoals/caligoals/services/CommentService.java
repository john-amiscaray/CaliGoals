package io.caligoals.caligoals.services;

import io.caligoals.caligoals.data.CommentRepo;
import io.caligoals.caligoals.dtos.CommentDto;
import io.caligoals.caligoals.entities.Comment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CommentService {

    private final CommentRepo commentRepo;
    private final PostService postService;
    private final UserService userService;

    @Autowired
    public CommentService(CommentRepo commentRepo, PostService postService, UserService userService){

        this.commentRepo = commentRepo;
        this.postService = postService;
        this.userService = userService;

    }

    public void addComment(CommentDto dto){

        Comment comment = new Comment(dto, postService, userService);
        commentRepo.save(comment);

    }


}
