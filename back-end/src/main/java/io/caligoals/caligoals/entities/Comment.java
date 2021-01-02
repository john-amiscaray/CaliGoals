package io.caligoals.caligoals.entities;

import io.caligoals.caligoals.dtos.CommentDto;
import io.caligoals.caligoals.services.PostService;
import io.caligoals.caligoals.services.UserService;

import javax.persistence.*;

@Entity
public class Comment {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long commentId;

    @ManyToOne
    private Post postReferringTo;

    @ManyToOne
    private User user;

    @Column(name="content", nullable = false)
    private String content;


    public Comment(){



    }

    public Comment(CommentDto dto, PostService postService, UserService userService){

        user = userService.getUser(dto.getUserId());
        postReferringTo = postService.getPost(dto.getPostId());
        content = dto.getContent();

    }

    public Long getCommentId() {
        return commentId;
    }

    public void setCommentId(Long commentId) {
        this.commentId = commentId;
    }

    public Post getPostReferringTo() {
        return postReferringTo;
    }

    public void setPostReferringTo(Post postReferringTo) {
        this.postReferringTo = postReferringTo;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    @Override
    public String toString() {
        return "Comment{" +
                "commentId=" + commentId +
                ", postReferringTo=" + postReferringTo +
                ", user=" + user +
                ", content='" + content + '\'' +
                '}';
    }
}
