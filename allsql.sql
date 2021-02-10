CREATE TABLE Software (
  ID_Software INT GENERATED ALWAYS AS IDENTITY,
  Name VARCHAR(100) NOT NULL,
  Scrum_master INT,
  QA INT
);

CREATE TABLE Version (
  ID_Version INT GENERATED ALWAYS AS IDENTITY,
  ID_Software INT,
  Suffix VARCHAR(100) DEFAULT "1.0",
  Release_date DATE,
  Improvements TEXT,
  State VARCHAR(20)
);
