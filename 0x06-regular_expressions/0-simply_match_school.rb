#!/usr/bin/env ruby

string = ARGV[0]
match = string.match(/School/)
if (match)
  puts match
else
  puts ""
end
