Feature: isbn-13 checksum validator
    
    Scenario Outline: user inputs isbn number
        Given user inputs isbn <number>
        When we run the validator
        Then the result should be <value>

        Examples:
        | number |  value |
        | 978-0-1825-6947-2 |   True |
        | 978-4-7222-5432-7 |  False |
        | 9789722273237     |   True |
        | 213-7-4321-54354  |  False |
        | 978 0 4722-8856 4 |   True |
        | 34244324          |  False |
        | 122 0 5436-8856 4 |  False |

