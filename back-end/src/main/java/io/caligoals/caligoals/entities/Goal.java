package io.caligoals.caligoals.entities;

import io.caligoals.caligoals.entities.compositekeys.GoalId;

import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Lob;
import java.sql.Timestamp;
import java.util.Arrays;

@Entity
public class Goal {

    @EmbeddedId
    private GoalId goalId;

    @Column(nullable = false, name="start_date")
    private Timestamp startDate;

    @Column(nullable = false, name="end_date")
    private Timestamp endDate;

    @Column(nullable = false, name="time_spent")
    private Long timeSpent;

    @Column(nullable = false, name="description")
    private String description;

    @Column(nullable = false, name="is_complete")
    private boolean isComplete;

    @Lob
    private byte[] goalIcon;

    public GoalId getGoalId() {
        return goalId;
    }

    public void setGoalId(GoalId goalId) {
        this.goalId = goalId;
    }

    public Timestamp getStartDate() {
        return startDate;
    }

    public void setStartDate(Timestamp startDate) {
        this.startDate = startDate;
    }

    public Timestamp getEndDate() {
        return endDate;
    }

    public void setEndDate(Timestamp endDate) {
        this.endDate = endDate;
    }

    public Long getTimeSpent() {
        return timeSpent;
    }

    public void setTimeSpent(Long timeSpent) {
        this.timeSpent = timeSpent;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public boolean isComplete() {
        return isComplete;
    }

    public void setComplete(boolean complete) {
        isComplete = complete;
    }

    public byte[] getGoalIcon() {
        return goalIcon;
    }

    public void setGoalIcon(byte[] goalIcon) {
        this.goalIcon = goalIcon;
    }

    @Override
    public String toString() {
        return "Goal{" +
                "goalId=" + goalId +
                ", startDate=" + startDate +
                ", endDate=" + endDate +
                ", timeSpent=" + timeSpent +
                ", description='" + description + '\'' +
                ", isComplete=" + isComplete +
                ", goalIcon=" + Arrays.toString(goalIcon) +
                '}';
    }
}
