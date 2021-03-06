package io.caligoals.caligoals.dtos;

import io.caligoals.caligoals.entities.Post;

public class PostDto {

    private Long postId;
    private String caption;
    private byte[] image;
    private Long userId;

    public PostDto(){



    }

    public PostDto(Post post){

        postId = post.getPostId();
        caption = post.getCaption();
        image = post.getImage();
        userId = post.getCreator().getUserId();

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

    public byte[] getImage() {
        return image;
    }

    public void setImage(byte[] image) {
        this.image = image;
    }

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    @Override
    public String toString() {
        return "PostDto{" +
                "postId=" + postId +
                ", caption='" + caption + '\'' +
                '}';
    }
}
