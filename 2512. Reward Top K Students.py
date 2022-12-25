import numpy as np
class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        student_score = []
        for studid in range(len(student_id)):
            report_f = report[studid]
            sept_report = report_f.split()
            studid_score = 0
            for repid in range(len(sept_report)):
                if sept_report[repid] in positive_feedback:
                    studid_score += 3
                elif sept_report[repid] in negative_feedback:
                    studid_score += -1
                else:
                    pass
            student_score.append(studid_score)

        rank_stu = []
        temp_stuscore = student_score
        ids = np.argsort(student_id)
        temp_stuscore = [temp_stuscore[i] for i in ids]
        student_id = [student_id[i] for i in ids]
        while any(i > -150 for i in temp_stuscore):
            max_stu = max(temp_stuscore)
            max_ind = temp_stuscore.index(max_stu)
            rank_stu.append(student_id[max_ind])
            temp_stuscore[max_ind] = -200


        return rank_stu[:k]



if __name__ == "__main__":
    positive_feedback = ["m","eveszfubew"]
    negative_feedback = ["iq","etwuedg","egpakyk","da","qkmhvgxg","q","zs","ujmy","mh"]
    report = ["eveszfubew jebebqp iq eveszfubew eveszfubew iq daej eveszfubew q da","ohfz zs ujmy egpakyk eveszfubew pffeq q qkmhvgxg kdgqq ipp","cceierguau mh da eveszfubew m etwuedg ikeft egpakyk ltnibxljfi m","km m iq rab inooo ujmy tlrdyu yqhn m xlkhebs","q etwuedg m eveszfubew ixrfzwmb m jyltumdwt dacmewk odbllqdiq eveszfubew"]
    student_id = [643903773,468275834,993893529,509587004,61125507]
    k = 5

    sol = Solution()
    result = sol.topStudents(positive_feedback = positive_feedback,
                    negative_feedback = negative_feedback,
                    report=report,
                    student_id=student_id,
                    k=k)
