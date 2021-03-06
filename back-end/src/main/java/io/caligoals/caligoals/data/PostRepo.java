package io.caligoals.caligoals.data;

import io.caligoals.caligoals.entities.Post;
import io.caligoals.caligoals.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PostRepo extends JpaRepository<Post, Long> {

    List<Post> findAllByCreator_Friends(User user);

}
