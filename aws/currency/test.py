
import concurrent.futures
import boto3

def worker(role_arn):

    credential = boto3.client('sts').assume_role(
        RoleArn=role_arn,
        RoleSessionName="assume_role_test"
    )

    session = boto3.session.Session(aws_access_key_id=credential['access_key'], aws_secret_access_key=credential['secret_key'], aws_session_token=credential['token'])

    instances = session.client('ec2').describe_instances()

    return True


def lambda_handler(event, context):
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for result in executor.map(worker, event.get("roles")):
            print(result)

if __name__ == "__main__":
    event = {
        "roles": [
            "arn:aws:iam::261912113761:role/AWSGo",
            "arn:aws:iam::932426754039:role/AWSGo",
            "arn:aws:iam::695366715288:role/AWSGo",
            "arn:aws:iam::598640774895:role/AWSGo",
            "arn:aws:iam::851914194101:role/AWSGo",
            "arn:aws:iam::894695242608:role/AWSGo",
            "arn:aws:iam::706225645189:role/AWSGo",
            "arn:aws:iam::357744277683:role/AWSGo",
            "arn:aws:iam::756410438932:role/AWSGo",
            "arn:aws:iam::309882183977:role/AWSGo",
            "arn:aws:iam::282405996381:role/AWSGo",
            "arn:aws:iam::621470250355:role/AWSGo",
            "arn:aws:iam::736111434131:role/AWSGo",
            "arn:aws:iam::215154503083:role/AWSGo",
            "arn:aws:iam::861587880549:role/AWSGo",
            "arn:aws:iam::120535867742:role/AWSGo",
            "arn:aws:iam::465649563607:role/AWSGo",
            "arn:aws:iam::669011675602:role/AWSGo",
            "arn:aws:iam::275669670840:role/AWSGo",
            "arn:aws:iam::761312330731:role/AWSGo",
            "arn:aws:iam::871595840017:role/AWSGo",
            "arn:aws:iam::811231682132:role/AWSGo",
            "arn:aws:iam::168146562322:role/AWSGo",
            "arn:aws:iam::812053965151:role/AWSGo",
            "arn:aws:iam::876055854555:role/AWSGo",
            "arn:aws:iam::928979556094:role/AWSGo",
            "arn:aws:iam::523360395272:role/AWSGo",
            "arn:aws:iam::403846302456:role/AWSGo",
            "arn:aws:iam::346471571170:role/AWSGo",
            "arn:aws:iam::107636557525:role/AWSGo",
            "arn:aws:iam::086389704194:role/AWSGo",
            "arn:aws:iam::417759954563:role/AWSGo",
            "arn:aws:iam::491032877027:role/AWSGo",
            "arn:aws:iam::811081544847:role/AWSGo",
            "arn:aws:iam::568547401107:role/AWSGo",
            "arn:aws:iam::184359800002:role/AWSGo",
            "arn:aws:iam::788747684760:role/AWSGo",
            "arn:aws:iam::257337402470:role/AWSGo",
            "arn:aws:iam::153725105438:role/AWSGo",
            "arn:aws:iam::854379373209:role/AWSGo",
            "arn:aws:iam::675601981640:role/AWSGo",
            "arn:aws:iam::787828630462:role/AWSGo",
            "arn:aws:iam::021817787677:role/AWSGo",
            "arn:aws:iam::479845013837:role/AWSGo",
            "arn:aws:iam::186426336459:role/AWSGo",
            "arn:aws:iam::882533951813:role/AWSGo",
            "arn:aws:iam::782171840433:role/AWSGo",
            "arn:aws:iam::754620929770:role/AWSGo",
            "arn:aws:iam::384148824847:role/AWSGo",
            "arn:aws:iam::552106289679:role/AWSGo",
            "arn:aws:iam::898468432231:role/AWSGo",
            "arn:aws:iam::463358726846:role/AWSGo",
            "arn:aws:iam::736111434131:role/AWSGo",
            "arn:aws:iam::215154503083:role/AWSGo",
            "arn:aws:iam::861587880549:role/AWSGo",
            "arn:aws:iam::120535867742:role/AWSGo",
            "arn:aws:iam::465649563607:role/AWSGo",
            "arn:aws:iam::669011675602:role/AWSGo",
            "arn:aws:iam::275669670840:role/AWSGo",
            "arn:aws:iam::761312330731:role/AWSGo",
            "arn:aws:iam::871595840017:role/AWSGo",
            "arn:aws:iam::811231682132:role/AWSGo",
            "arn:aws:iam::168146562322:role/AWSGo",
            "arn:aws:iam::812053965151:role/AWSGo",
            "arn:aws:iam::876055854555:role/AWSGo",
            "arn:aws:iam::928979556094:role/AWSGo",
            "arn:aws:iam::523360395272:role/AWSGo",
            "arn:aws:iam::403846302456:role/AWSGo",
            "arn:aws:iam::346471571170:role/AWSGo",
            "arn:aws:iam::107636557525:role/AWSGo",
            "arn:aws:iam::086389704194:role/AWSGo",
            "arn:aws:iam::417759954563:role/AWSGo",
            "arn:aws:iam::491032877027:role/AWSGo",
            "arn:aws:iam::811081544847:role/AWSGo",
            "arn:aws:iam::568547401107:role/AWSGo",
            "arn:aws:iam::184359800002:role/AWSGo",
            "arn:aws:iam::788747684760:role/AWSGo",
            "arn:aws:iam::257337402470:role/AWSGo",
            "arn:aws:iam::153725105438:role/AWSGo",
            "arn:aws:iam::854379373209:role/AWSGo",
            "arn:aws:iam::675601981640:role/AWSGo",
            "arn:aws:iam::787828630462:role/AWSGo",
            "arn:aws:iam::021817787677:role/AWSGo",
            "arn:aws:iam::479845013837:role/AWSGo",
            "arn:aws:iam::186426336459:role/AWSGo",
            "arn:aws:iam::882533951813:role/AWSGo",
            "arn:aws:iam::782171840433:role/AWSGo",
            "arn:aws:iam::754620929770:role/AWSGo",
            "arn:aws:iam::384148824847:role/AWSGo",
            "arn:aws:iam::552106289679:role/AWSGo",
            "arn:aws:iam::898468432231:role/AWSGo",
            "arn:aws:iam::463358726846:role/AWSGo",
            "arn:aws:iam::940478797813:role/AWSGo",
            "arn:aws:iam::806778360109:role/AWSGo",
            "arn:aws:iam::950533882610:role/AWSGo",
            "arn:aws:iam::301481189126:role/AWSGo",
            "arn:aws:iam::431525257644:role/AWSGo",
            "arn:aws:iam::012088573068:role/AWSGo",
            "arn:aws:iam::342586268637:role/AWSGo",
            "arn:aws:iam::293950251116:role/AWSGo",
            "arn:aws:iam::293356008345:role/AWSGo",
            "arn:aws:iam::935135781143:role/AWSGo",
            "arn:aws:iam::783686394728:role/AWSGo",
            "arn:aws:iam::709696132558:role/AWSGo"
        ]
    }
    lambda_handler(event, None)


