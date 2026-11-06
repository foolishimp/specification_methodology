def admitted(issuer_grant, recipient_grant, evidence_current):
    return (issuer_grant or recipient_grant) and evidence_current
