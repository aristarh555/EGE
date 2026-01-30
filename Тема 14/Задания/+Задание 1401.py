for x in range(13):
    for y in range(13):
        p1 = y + 8*13**1 + 7*13**2 + x*13**3 + 8*13**4
        p2 = 7 + y*18**1 + x*18**2 + 9*18**3 + 7*18**4
        r = p1 + p2
        if r % 9 == 0:
            print(r, r/9)
            break






answer = 113024

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1401, answer, '436fc6a87245490c1c09148823eec9ff'))