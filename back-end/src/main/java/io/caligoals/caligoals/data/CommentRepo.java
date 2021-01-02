package io.caligoals.caligoals.data;

import io.caligoals.caligoals.entities.Comment;
import io.caligoals.caligoals.entities.Post;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CommentRepo extends JpaRepository<Comment, Long> {

    List<Comment> findAllByPostReferringTo(Post post);

}
