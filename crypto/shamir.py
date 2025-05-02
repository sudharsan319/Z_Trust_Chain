from Crypto.Protocol.SecretSharing import Shamir

def generate_shares(secret, threshold, num_shares):
    shares = Shamir.split(threshold, num_shares, secret)
    return shares

def reconstruct_secret(shares):
    return Shamir.combine(shares)
