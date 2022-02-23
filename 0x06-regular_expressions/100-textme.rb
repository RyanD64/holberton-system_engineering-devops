#!/usr/bin/env ruby
info = ARGV[0].scan(/\[from:(.+?)\]|\[to:(.+?)\]|\[flags:(.+?)\]/)
list = [info[0].compact, info[1].compact, info[2].compact]
puts list.join(',')
