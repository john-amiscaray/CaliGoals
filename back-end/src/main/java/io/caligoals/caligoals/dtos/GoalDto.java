package io.caligoals.caligoals.dtos;


import io.caligoals.caligoals.entities.Goal;

public class GoalDto {

    private Long userId;
    private String title;
    private Long startDate;
    private Long endDate;
    private Long timeSpent;
    private Long timeNeeded;
    private String description;
    private boolean isComplete;


    public GoalDto() {
    }

    public GoalDto(Goal goal) {

        userId = goal.getGoalId().getUser().getUserId();
        title = goal.getGoalId().getTitle();
        startDate = goal.getStartDate().getTime();
        endDate = goal.getEndDate().getTime();
        timeSpent = goal.getTimeSpent();
        description = goal.getDescription();
        isComplete = goal.isComplete();
        timeNeeded = goal.getTimeNeeded();

    }

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Long getStartDate() {
        return startDate;
    }

    public void setStartDate(Long startDate) {
        this.startDate = startDate;
    }

    public Long getEndDate() {
        return endDate;
    }

    public void setEndDate(Long endDate) {
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

    public Long getTimeNeeded() {
        return timeNeeded;
    }

    public void setTimeNeeded(Long timeNeeded) {
        this.timeNeeded = timeNeeded;
    }
}
