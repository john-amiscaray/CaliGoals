package io.caligoals.caligoals.services;

import io.caligoals.caligoals.data.UserRepo;
import io.caligoals.caligoals.dtos.UserDto;
import io.caligoals.caligoals.entities.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

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

    public void setProfilePicture(Long userId, MultipartFile file){

        User user = getUser(userId);
        try {
            user.setProfilePicture(file.getBytes());
            updateUser(user);
        }catch(IOException ex){
            System.out.println("Whoops an IOException happened");
        }
    }

    public void updateUser(User user){

        Optional<User> check_exists = userRepo.findById(user.getUserId());

        if(check_exists.isPresent()){

            userRepo.save(user);

        }else{

            throw new IllegalArgumentException("Can't update user that does not exist.");

        }

    }

    public List<UserDto> getFriends(Long userId){

        User user = getUser(userId);
        List<UserDto> friends = userRepo.findAllByFriendsContaining(user).stream()
                .map(UserDto::new)
                .collect(Collectors.toList());
        friends.forEach(friend -> friend.setPassword(""));
        return friends;

    }

    public void addAsFriend(Long sender, Long receiver){

        User user = getUser(receiver);
        User newFriend = getUser(sender);
        user.getFriends().add(newFriend);
        newFriend.getFriends().add(user);
        updateUser(user);
        updateUser(newFriend);

    }


    public void addToGrowthAmount(Long time, Long userId){

        User user = getUser(userId);
        user.setGrowthAmount(user.getGrowthAmount() + time);
        updateUser(user);

    }

    public Long getGrowthAmount(Long userId){

        User user = getUser(userId);
        return user.getGrowthAmount();

    }


}
