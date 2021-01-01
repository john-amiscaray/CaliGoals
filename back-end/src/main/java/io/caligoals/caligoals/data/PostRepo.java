package io.caligoals.caligoals.data;

import io.caligoals.caligoals.entities.Post;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PostRepo extends JpaRepository<Post, Long> {
}
