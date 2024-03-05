# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "K Means is relatively more sensitive to outliers"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "If the initial random centres were different we would end up having different clusters"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "It might take less memory and time, but not as efficient as agglomerative clusterings"

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "We will reassign the points to the respective clusters in the post process."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In term of K Means the sum of SSE and SSB is constant, so if one increases the other should decreases"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "Yes its true, the SSB + SSE = constant, if one increases the other will decrease."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "The statement constrast the similarity, SSE+ SSB = constant"

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "It is true, if the distance between clusters are increasing, the points with in a cluster more likely to form a class, so SSB will reduce as the compliment to raise in SSE, so overall it will be a constant"

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "It is possible that increase in cohesion will make the cluster move further away."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Yes because the initial clusters are already for away and lies within the best candidate clusters."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K Means couldn't guarantee that it could give optimal results in case of overlapping or convolutated data"

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The final Cluster centroids will be 8.5, 16.5, 12.5 so the 12.5 cluster is far away from other points so it should be left empty"

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10* R **2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As the points in the A will drag a centre from B and so does the C, but due to much variance from points C, A will not get centre from B."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Due to the points already present in A, centroid in A will remain the same, one of the ponits in B gets pulled by the C cluster due to its high intensity."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Its possible that the middle point between the 2 circles A and B might be the final centroid, and the other 2 centroids might stay in C, because if the points stays between A and B that would lead to minimize the variance."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The smallest distance between all possible distances(from groups), the lowest was from Group A to Group B"

    # type: set
    answers["(b)"] = {"Group A","Group C"}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The smallest distance between the farthest points in all possiblities is between A and C clusters"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {"B","C","E","F","I","J","L","M"}

    # type: set
    answers["(a) boundary"] = {"D","G"}

    # type: set
    answers["(a) noise"] = {"A","H"}

    # type: set
    answers["(b) cluster 1"] = set()

    # type: set
    answers["(b) cluster 2"] = {"B","D","C","E","F","G"}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = {"I","J","L","M"}

    # type: set

    answers["(c)-a core"] = {"B","C","D","E","F","G","I","J","L","M"}

    # type: set
    answers["(c)-a boundary"] = {"A","H"}

    # type: set
    answers["(c)-a noise"] =set()

    # type: set
    answers["(c)-b cluster 1"] = set()

    # type: set
    answers["(c)-b cluster 2"] = {"A","B","C","D","E","F","G","H","I","J","L","M"}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "More samples leads to more impurity"

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Least impurity even though it looks like we have it in case of cluster 2, but due to a large number of samples from water column in cluster 1 we will choose it"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "We could see all diagonal squares has the strong correlation and dark blue which represent on the legend shown has strong relationship"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The off diagonal elements doesn't overlap with immediate neighbors which means that they doesn;t have any other relationship with other clusters"

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The relation in B and in C are strong and for A and D its relatively weak so they has lighter blue shade"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "We could see a 2*2 matrix at each 2 strides along the diagonal which includes off diagonal elements, indicating the pattern in X, as A and B close they have a slight blue, B and C close they do have the blue shade, similarly for the C and D which are close we could see a 2x2 light blue shade in the bottom right of Matrix 2"

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The relation in B and in C are strong and for A and D its relatively weak so they has lighter blue shade"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "If we draw a horizontal line along y axis lets say that seperates the A,B,C as one group and D as other, and that makes the first 3 has a good relationship among themselves and D had relatively little to no relationship with other set (A,B,C), this is why we could see a seperate 3X3 in Matrix 3." 

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "A had strong relation with itself, then followed by B, C and D descending order of relationship"

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "B had strong relation with itself, then followed by A, C and D descending order of relationship"

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "C had strong relation with itself, then followed by D, B and A descending order of relationship"

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "D had strong relation with itself, then followed by C, B and A descending order of relationship"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["hierarchical","overlapping","partial"]

    # type: list
    answers["(b)"] = ["partitional","fuzzy","complete"]
    answers['(b) explain']="the patients are either belong to one group or the other so its exclusive, and as the doctor had all the things we will be classified into one of them thats why its a complete not the partial."

    # type: list
    answers["(c)"] = ["hierarchical","overlapping","complete"]
    answers['(c) explain']="If a student does RA, TA and some other non academic job, then sure does it has hierarchical structure, as he/she has multiple job categories overlapping is suitable in that case."

    # type: list
    answers["(d)"] = ["hierarchical","overlapping","partial"]
    answers['(d) explain']="If the deparments are under the college"

    # type: list
    answers["(e)"] = ["partitional","exclusive","partial"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "There's no hierarchy associated with it, and either student had the grade or not so its exclusive, and asked for all students in CS but not all students in CS had the course, so its partial instead of complete."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN can distingush complex and convoluted datasets and its the case in b where the density of eyes, nose and mouth are almost similar so it could distinguish them properly."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "KMeans cant gurantee that it could find the all the mentioned successfully, as the points are convoluted so its harder to KMeans to find them in case of a, but it might successfully end up in finding in (b) as if the centers start at the eyes, nose and mouth."

    # type: string
    answers["(c)"] = "DBSCAN, but in case of Figure A, if we could flip the density shown in the other way around we could get the same image as in B, so that we could apply DBSCAN over the modified image to detect the nose, etc."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
