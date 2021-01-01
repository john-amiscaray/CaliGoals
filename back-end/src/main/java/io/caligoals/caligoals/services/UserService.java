package io.caligoals.caligoals.services;

import io.caligoals.caligoals.data.UserRepo;
import io.caligoals.caligoals.dtos.UserDto;
import io.caligoals.caligoals.entities.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    private final UserRepo userRepo;
    private final BCryptPasswordEncoder bcryptPasswordEncoder;

    @Autowired
    public UserService(UserRepo userRepo, BCryptPasswordEncoder bcryptPasswordEncoder){

        this.userRepo = userRepo;
        this.bcryptPasswordEncoder = bcryptPasswordEncoder;

    }

    public User getUser(Long userId){

        return userRepo.findById(userId).orElseThrow();

    }

    public User getUser(String username){

        return userRepo.findUserByUsername(username).orElseThrow();

    }

    public void saveUser(UserDto dto){

        User user = new User(dto, bcryptPasswordEncoder);
        userRepo.save(user);

    }


}
