Feature: knowledge checker for roman numerals
    
    Scenario Outline: user inputs numbers and his guess
        Given user inputs <number> and <guess>
        When we run the converter
        Then the result should be <value>

        Examples:
        | number |     guess |  value |
        |      1 |         I |   True |
        |      2 |       III |  False |
        |   1972 |  MCMLXXII |   True |
        |   2137 | MMCXXXVII |   True |
        |   2137 |  MMCXXXVI |  False |
        |     55 |fifty-five |  False |
        |      5 |      five |  False |

