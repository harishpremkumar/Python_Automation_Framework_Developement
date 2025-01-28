Feature: Verify GitHub page

  Scenario: Count occurrences of 'GitHub' on the page
    Given I open the GitHub page
    When I get the word count for "GitHub"
    Then I should see "GitHub" appear more than 0 times
