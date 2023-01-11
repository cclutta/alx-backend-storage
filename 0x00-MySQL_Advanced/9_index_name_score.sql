-- that creates an index idx_name_first_score, first letter of name and score

CREATE INDEX idx_name_first_score on names(name(1), score)

