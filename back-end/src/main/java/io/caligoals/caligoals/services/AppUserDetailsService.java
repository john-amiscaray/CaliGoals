package io.caligoals.caligoals.services;

import io.caligoals.caligoals.data.UserRepo;
import io.caligoals.caligoals.dtos.AppUserDetails;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

public class AppUserDetailsService implements UserDetailsService {

    @Autowired
    private UserRepo repo;

    @Override
    public UserDetails loadUserByUsername(String s) throws UsernameNotFoundException {

        return new AppUserDetails(repo.findUserByUsername(s).orElseThrow());
    }
}
