package io.caligoals.caligoals.entities;

import io.caligoals.caligoals.dtos.UserDto;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import javax.persistence.*;
import java.util.Arrays;
import java.util.List;

@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long userId;

    @Column(name="username", nullable = false, length = 30, unique = true)
    private String username;

    @Column(nullable = false, name="pass")
    private String password;

    @ManyToMany
    private List<User> friends;

    @Column(name="growth_amount", nullable = false)
    private Long growthAmount;

    @Lob
    private byte[] profilePicture;

    @OneToMany
    private List<Post> posts;

    @OneToMany(mappedBy = "goalId.user")
    private List<Goal> goals;

    public User(UserDto userDto, BCryptPasswordEncoder encoder){

        userId = userDto.getUserId();
        username = userDto.getUsername();
        password = encoder.encode(userDto.getPassword());
        growthAmount = 0L;

    }

    public User(){




    }

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<User> getFriends() {
        return friends;
    }

    public void setFriends(List<User> friends) {
        this.friends = friends;
    }

    public Long getGrowthAmount() {
        return growthAmount;
    }

    public void setGrowthAmount(Long growthAmount) {
        this.growthAmount = growthAmount;
    }

    public byte[] getProfilePicture() {
        return profilePicture;
    }

    public void setProfilePicture(byte[] profilePicture) {
        this.profilePicture = profilePicture;
    }

    public List<Post> getPosts() {
        return posts;
    }

    public void setPosts(List<Post> posts) {
        this.posts = posts;
    }

    public List<Goal> getGoals() {
        return goals;
    }

    public void setGoals(List<Goal> goals) {
        this.goals = goals;
    }

//    @Override
//    public String toString() {
//        return "User{" +
//                "userId=" + userId +
//                ", username='" + username + '\'' +
//                ", password='" + password + '\'' +
//                ", friends=" + friends +
//                ", growthAmount=" + growthAmount +
//                ", profilePicture=" + Arrays.toString(profilePicture) +
//                ", posts=" + posts +
//                ", goals=" + goals +
//                '}';
//    }
}
