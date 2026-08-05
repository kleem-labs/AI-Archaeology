def idempotent(key,operation,records):
 if key not in records: records[key]=operation()
 return records[key]
