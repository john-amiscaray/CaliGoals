package io.caligoals.caligoals.entities;

import io.caligoals.caligoals.dtos.PostDto;
import io.caligoals.caligoals.services.UserService;

import javax.persistence.*;
import java.util.Arrays;
import java.util.List;

@Entity
public class Post {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long postId;

    @Column(name="caption", nullable = false)
    private String caption;

    @OneToMany(mappedBy = "postReferringTo")
    private List<Comment> comments;

    @Lob
    private byte[] image;

    @ManyToOne
    private User creator;

    public Post(){


    }

    public Post(PostDto dto, UserService userService){

        postId = dto.getPostId();
        caption = dto.getCaption();
        creator = userService.getUser(dto.getUserId());

    }

    public Long getPostId() {
        return postId;
    }

    public void setPostId(Long postId) {
        this.postId = postId;
    }

    public String getCaption() {
        return caption;
    }

    public void setCaption(String caption) {
        this.caption = caption;
    }

    public List<Comment> getComments() {
        return comments;
    }

    public void setComments(List<Comment> comments) {
        this.comments = comments;
    }

    public byte[] getImage() {
        return image;
    }

    public void setImage(byte[] image) {
        this.image = image;
    }

    public User getCreator() {
        return creator;
    }

    public void setCreator(User creator) {
        this.creator = creator;
    }

    @Override
    public String toString() {
        return "Post{" +
                "postId=" + postId +
                ", caption='" + caption + '\'' +
                ", comments=" + comments +
                ", image=" + Arrays.toString(image) +
                '}';
    }
}
