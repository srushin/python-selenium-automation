# Created by srushin at 11/25/24
Feature: Tests for Target page

  Scenario: Verify Empty Target Cart
    Given Open Target Page
    When Navigate to Cart
    Then Verify Cart is Empty Message

  Scenario: Verify Target Sign in
    Given Open Target Page
    When Click Sign In
    When Side Sign In
    Then Verify Sign In Page