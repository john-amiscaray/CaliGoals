package io.caligoals.caligoals.entities.compositekeys;

import io.caligoals.caligoals.entities.User;

import javax.persistence.Embeddable;
import javax.persistence.ManyToOne;
import java.io.Serializable;
import java.util.Objects;

@Embeddable
public class GoalId implements Serializable {

    @ManyToOne
    private User user;

    private String title;


    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        GoalId goalId = (GoalId) o;
        return user.equals(goalId.user) && title.equals(goalId.title);
    }

    @Override
    public int hashCode() {
        return Objects.hash(user, title);
    }
}
