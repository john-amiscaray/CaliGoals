package io.caligoals.caligoals.entities;

import io.caligoals.caligoals.dtos.GoalDto;
import io.caligoals.caligoals.entities.compositekeys.GoalId;
import io.caligoals.caligoals.services.UserService;

import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Lob;
import java.sql.Date;
import java.util.Arrays;

@Entity
public class Goal {

    @EmbeddedId
    private GoalId goalId;

    @Column(nullable = false, name="start_date")
    private Date startDate;

    @Column(nullable = false, name="end_date")
    private Date endDate;

    @Column(nullable = false, name="time_needed")
    private Long timeNeeded;

    @Column(nullable = false, name="time_spent")
    private Long timeSpent;

    @Column(nullable = false, name="description")
    private String description;

    @Column(nullable = false, name="is_complete")
    private boolean isComplete;

    @Lob
    private byte[] goalIcon;

    public Goal(){


    }

    public Goal(GoalDto dto, UserService service){

        description = dto.getDescription();
        timeSpent = dto.getTimeSpent();
        goalId = new GoalId(service.getUser(dto.getUserId()), dto.getTitle());
        isComplete = dto.isComplete();
        startDate = new Date(dto.getStartDate());
        endDate = new Date(dto.getEndDate());
        timeNeeded = dto.getTimeNeeded();

    }

    public GoalId getGoalId() {
        return goalId;
    }

    public void setGoalId(GoalId goalId) {
        this.goalId = goalId;
    }

    public Date getStartDate() {
        return startDate;
    }

    public void setStartDate(Date startDate) {
        this.startDate = startDate;
    }

    public Date getEndDate() {
        return endDate;
    }

    public void setEndDate(Date endDate) {
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

    public Long getTimeNeeded() {
        return timeNeeded;
    }

    public void setTimeNeeded(Long timeNeeded) {
        this.timeNeeded = timeNeeded;
    }

    @Override
    public String toString() {
        return "Goal{" +
                "goalId=" + goalId +
                ", startDate=" + startDate +
                ", endDate=" + endDate +
                ", timeNeeded=" + timeNeeded +
                ", timeSpent=" + timeSpent +
                ", description='" + description + '\'' +
                ", isComplete=" + isComplete +
                ", goalIcon=" + Arrays.toString(goalIcon) +
                '}';
    }
}
