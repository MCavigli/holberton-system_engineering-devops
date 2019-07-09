#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)\+?\S*(?<!\])|(?<=to:)\+?\d*(?<!\])|(?<=flags:)\S*(?<!\])/).join(',')
