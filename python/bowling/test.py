"""
* Rule A. The score for a frame is the total pins bowled over during that frame, if the number is less than ten (an open frame, or error or split depending some other rules beyond the scope of this problem).
* Rule B. If all ten pins are bowled over on the first delivery (a strike), the score for that frame is 10 + the next two deliveries.
* Rule C. If all ten pins are bowled over between the first two deliveries (a spare), the score for that frame is 10 + the next delivery.

Frame	First delivery	Second delivery	Scoring rule	                                                                            Frame Score	Total
1	    8	            2	            C- spare = 10 + next delivery	                                                            19	        19
2       9	            -	            A- open = 9	                                                                                9	        28
3	    10	            (not taken)	    B- strike = 10 + next 2 deliveries	                                                        26	        54
4	    10	            (not taken)	    B- strike = 10 + next 2 deliveries	                                                        20	        74
5	    6	            4	            C- spare = 10 + next delivery	                                                            14	        88
6	    4	            6	            C- spare = 10 + next delivery	                                                            20	        108
7	    10	            (not taken)	    B- strike = 10 + next 2 deliveries	                                                        28	        136
8	    8	            -	            A- open = 8	                                                                                8	        144
9	    10	            (not taken)	    B- strike = 10 + next 2 deliveries	                                                        30	        174
10	    10	            10 and 10	    B- strike = 10 + next 2 deliveries, two extra deliveries are taken during this 10th frame.	30	        204
"""
from pprint import pprint
import logging


class BowlingGame:
    def __init__(self, scores: list):
        self.frames = self.process(scores)
        self.total = self.frames[-1]["total"]

    def process(self, scores):
        frames = []
        total = 0
        # loop in 10 frames
        for index in range(10):
            thorws = scores[index]
            base_score = sum(thorws)
            bunous_score = 0
            type = "open"
            if base_score == 10:
                if len(thorws) == 1:  # strike
                    bunous_score = scores[index + 1][0] + scores[index + 2][0]
                    type = "strike"
                else:  # spare
                    bunous_score = scores[index + 1][0]
                    type = "spare"

            frame_score = base_score + bunous_score

            total = total + frame_score
            frames.append(
                {
                    "no": index + 1,
                    "type": type,
                    "thorws": thorws,
                    "base": base_score,
                    "bunous": bunous_score,
                    "score": frame_score,
                    "total": total,
                }
            )

        return frames

    def show(self):
        pprint(self.frames)
        pprint(self.total)


if __name__ == "__main__":
    data = [[8, 2], [9], [10], [10], [6, 4], [4, 6], [10], [8], [10], [10], [10], [10]]

    game = BowlingGame(data)
    game.show()
