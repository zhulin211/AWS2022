import boto3
s3 = boto3.client('s3')

r = s3.select_object_content(
        # Bucket='aws2022-s3-basic',
        Bucket='qytangaws2022s3',
        # GUI创建的S3
        Key='select.csv',
        ExpressionType='SQL',
        # Expression="select s._1, s._2 from s3object s where s._1 = 'tina'",   # 第一列的值为'tina'
        # Expression="select * from s3object s where s._1 = 'tina'",            # 第一列的值为'tina'
        Expression="select * from s3object s where CAST(s._2 as INT) > 15000",  # 第二列的值大于15000
        InputSerialization={'CSV': {}},
        OutputSerialization={'CSV': {}},
)
for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        result_list = []
        for line in records.split('\n'):
            if line:
                result_list.append(line.split(','))
        print(result_list)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])
