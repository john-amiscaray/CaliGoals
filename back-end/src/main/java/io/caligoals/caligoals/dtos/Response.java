package io.caligoals.caligoals.dtos;

public class Response {

    private Object message;

    public Response(){ }

    public Response(Object message){

        this.message = message;

    }

    public Object getMessage() {
        return message;
    }

    public void setMessage(Object message) {
        this.message = message;
    }
}
