package io.caligoals.caligoals.dtos;

import io.caligoals.caligoals.entities.Comment;

public class CommentDto {

    private Long commentId;
    private Long postId;
    private Long userId;
    private String content;

    public CommentDto(){


    }

    public CommentDto(Comment comment){

        commentId = comment.getCommentId();
        postId = comment.getPostReferringTo().getPostId();
        userId = comment.getUser().getUserId();
        content = comment.getContent();

    }

    public Long getCommentId() {
        return commentId;
    }

    public void setCommentId(Long commentId) {
        this.commentId = commentId;
    }

    public Long getPostId() {
        return postId;
    }

    public void setPostId(Long postId) {
        this.postId = postId;
    }

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    @Override
    public String toString() {
        return "CommentDto{" +
                "commentId=" + commentId +
                ", postId=" + postId +
                ", userId=" + userId +
                ", content='" + content + '\'' +
                '}';
    }
}
