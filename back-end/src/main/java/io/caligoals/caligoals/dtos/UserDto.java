package io.caligoals.caligoals.dtos;

import io.caligoals.caligoals.entities.User;

import java.util.Arrays;

public class UserDto {

    private Long userId;
    private String username;
    private String password;
    private Long growthAmount;
    private byte[] profilePicture;

    public UserDto(User user){

        userId = user.getUserId();
        username = user.getUsername();
        password = user.getPassword();
        growthAmount = user.getGrowthAmount();
        profilePicture = user.getProfilePicture();

    }

    public UserDto(){ }


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

    @Override
    public String toString() {
        return "UserDto{" +
                "userId=" + userId +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", growthAmount=" + growthAmount +
                ", profilePicture=" + Arrays.toString(profilePicture) +
                '}';
    }
}
