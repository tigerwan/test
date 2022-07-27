def max_printable_documents(documents: list, is_malfunctioning: list, x: int) -> int:
    # Write your code here
    docs = []
    malfunctioning_length = len(is_malfunctioning)
    for i in range(min(malfunctioning_length -x + 2,malfunctioning_length)):
        if is_malfunctioning[i] is True:
            doc = []
            doc += [ documents[j] for j in range(i) if is_malfunctioning[j] is False]
            if i+x >= malfunctioning_length:
                doc += documents[i: malfunctioning_length]
            else:
                doc += documents[i: i+x]
                doc += [ documents[j] for j in range(i+x,len(documents)) if is_malfunctioning[j] is False]

            # print('++++++++++++++++++++++++++')
            # print('inde: {}'.format(i))
            # print('sum:{}'.format(sum(doc)))
            # print('doc:{}'.format(doc))

            docs.append(doc)

    sums = [sum(x) for x in docs]

    return max(sums) if len(sums) else 0





if __name__ == '__main__':
    print(max_printable_documents([5,0,1,3,1,6,2],[False,True,True,False,False,True,False],2))
    print(max_printable_documents([1,0,4,2,0,3],[True,False,True,False,True,False],3))
