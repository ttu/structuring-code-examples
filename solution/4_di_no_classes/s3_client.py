from packages import requests


S3_USERNAME = ""
S3_PASSWORD = ""
S3_STORAGE_BUCKET = ""


class S3Client(object):

    def store_label(self, encoded_label: bytes):
        s3_response = requests.post(
            f"https://dev.aws.com/s3/{S3_STORAGE_BUCKET}",
            data=encoded_label,
            auth=requests.auth.HTTPBasicAuth(S3_USERNAME, S3_PASSWORD),
            headers={"Content-Type": "application/octet-stream",
                     "Accept": "application/json"},
        )

        if s3_response.status_code != 200:
            return False, "S3 error"

        s3_response_json = s3_response.json()
        return True, s3_response_json["Location"]
