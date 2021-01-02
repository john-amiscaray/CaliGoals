package io.caligoals.caligoals.data;

import io.caligoals.caligoals.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface UserRepo extends JpaRepository<User, Long> {

    Optional<User> findUserByUsername(String username);

    List<User> findAllByFriendsContaining(User user);

}
