package io.caligoals.caligoals.services;

import io.caligoals.caligoals.data.CommentRepo;
import io.caligoals.caligoals.data.PostRepo;
import io.caligoals.caligoals.data.UserRepo;
import io.caligoals.caligoals.dtos.PostDto;
import io.caligoals.caligoals.entities.Comment;
import io.caligoals.caligoals.entities.Post;
import io.caligoals.caligoals.entities.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class PostService {

    private final PostRepo postRepo;
    private final UserRepo userRepo;
    private final CommentRepo commentRepo;
    private final UserService userService;

    @Autowired
    public PostService(PostRepo postRepo, UserRepo userRepo, CommentRepo commentRepo, UserService userService){

        this.postRepo = postRepo;
        this.userRepo = userRepo;
        this.commentRepo = commentRepo;
        this.userService = userService;

    }

    public Post addPost(PostDto dto){

        Post p = new Post(dto, userService);
        postRepo.save(p);
        return p;

    }

    public Post getPost(Long postId){

        return postRepo.findById(postId).orElseThrow();

    }

    public void setImage(Long postId, MultipartFile file, Long userId) throws IllegalAccessException {

        Post post = getPost(postId);
        User user = userRepo.findById(userId).orElseThrow();
        if(user.getPosts().contains(post)){

            try {
                post.setImage(file.getBytes());
                updatePost(post);
            }catch(IOException ex){
                System.out.println("Whoops an IOException happened");
            }
        }else{

            throw new IllegalAccessException("You cannot modify someone else's post");
        }
    }

    public void updatePost(Post post){

        Optional<Post> check_exists = postRepo.findById(post.getPostId());

        if(check_exists.isPresent()){

            postRepo.save(post);

        }else{

            throw new IllegalArgumentException("Can't update user that does not exist.");

        }

    }

    public List<Comment> getComments(Long postId){

        Post post = getPost(postId);
        return commentRepo.findAllByPostReferringTo(post);

    }

    public List<PostDto> getFeed(Long userId){

        return postRepo.findAllByCreator_Friends(userRepo.findById(userId).orElseThrow()).stream()
                .map(PostDto::new)
                .collect(Collectors.toList());

    }

}
