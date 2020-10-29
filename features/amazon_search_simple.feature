Feature: Amazon Search

Scenario: User navigates to Amazon home page and make a search for "Nike Airmax"

Given user is on the Amazon web site
When user clicks in the search field and enters "Nike Airmax"
And user clicks on search icon
Then new page with "Nike Airmax" results and title is displayed
