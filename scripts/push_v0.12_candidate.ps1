git push -u origin build/v0.12.0
if ($LASTEXITCODE -ne 0) { throw "Push failed" }
