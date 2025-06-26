Feature: Verify registration functionality

    @Sanity
    Scenario Outline: Registration with valid data
        Given User is on registration page
        When User enters username "<username>"
        And User enters email "<email>"
        And User enters password "<password>"
        And User click the signup button
        Then Usser should be registered successfully

    Examples:
        | username | password | email |
        | User1  | Password1  | User1@gmail.com  |