-- Thunderbird DESKTOP SUMO questions, monthly counts, from the SUMO BigQuery
-- ground-truth table. Used to validate this repo's / the aaq-scraper's counts
-- (see README.md and issue #67). No BigQuery API access from CI — run this in the
-- BQ console and export the result as CSV.
--
-- Matches the repo's counting: product = 'thunderbird' (desktop; excludes
-- thunderbird-android), spam dropped, deduped on question_id, bucketed by the
-- UTC month of created_utc (same DATETIME(created_utc) expression the ad-hoc
-- per-month query used).

SELECT
  FORMAT_DATETIME('%Y-%m', DATETIME(created_utc)) AS month,
  COUNT(DISTINCT question_id)                     AS num_questions
FROM
  `moz-fx-sumo-prod.sumo.metrics_thunderbird_questions`
WHERE
  product LIKE 'thunderbird'          -- exact match: desktop only, not thunderbird-android
  AND is_spam = FALSE
  AND DATETIME(created_utc) >= DATETIME '2023-01-01'
  AND DATETIME(created_utc) <  DATETIME '2026-08-01'
GROUP BY
  month
ORDER BY
  month;

-- Yearly variant: swap the SELECT/GROUP BY month for:
--   FORMAT_DATETIME('%Y', DATETIME(created_utc)) AS year, COUNT(DISTINCT question_id) ...
--   GROUP BY year ORDER BY year;
