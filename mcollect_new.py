import psutil
import time



collect_data = 3000
collect_data_freq = 1


counter = 0


header = "cpu_percent,cpu_user_time,cpu_system_time,cpu_idle_time,cpu_iowait,cpu_irq,cpu_softirq,cpu_numbers_of_ctx_switches,cpu_numbers_of_interrupts,cpu_numbers_of_soft_interrupts,"
header = header + "cpu_load_runable_state,memory_percent,memory_active,memory_buffers,memory_cached,memory_shared,memory_swap_percent,memory_swap_sin,memory_swap_sout,disk_usage_percent,disk_read_count,"
header = header + "disk_write_count,disk_read_time,disk_write_time,disk_busy_time,network_bytes_sent,network_bytes_recv,network_packets_sent,network_packets_recv,network_errin,network_errout,"
header = header + "network_dropin,network_dropout\n"


#header = "cpu_percent,memory_percent,disk_usage_percent\n"

print(header)

f = open("dump.csv", "w")
f.write(header)
f.close()


while counter < collect_data:
	counter = counter + 1
	time.sleep(collect_data_freq)


	cpu_percent = str(psutil.cpu_percent(1))
	cpu = psutil.cpu_times()
	cpu_user_time = str(cpu[0])
	cpu_system_time = str(cpu[2])
	cpu_idle_time = str(cpu[3])
	cpu_iowait = str(cpu[4])
	cpu_irq = str(cpu[5])
	cpu_softirq = str(cpu[6])
	cpu_stats = psutil.cpu_stats()
	cpu_numbers_of_ctx_switches = str(cpu_stats[0])
	cpu_numbers_of_interrupts = str(cpu_stats[1])
	cpu_numbers_of_soft_interrupts = str(cpu_stats[2])
	cpu_load_runable_state = str(psutil.getloadavg()[1])

	memory = psutil.virtual_memory()
	memory_percent = str(memory[2])
	memory_active = str(memory[5])
	memory_buffers = str(memory[7])
	memory_cached = str(memory[8])
	memory_shared = str(memory[9])
	memory_swap = psutil.swap_memory()
	memory_swap_percent = str(memory_swap[3])
	memory_swap_sin = str(memory_swap[4])
	memory_swap_sout = str(memory_swap[5])

	disk_usage_percent = str(psutil.disk_usage('/')[3])
	disk = psutil.disk_io_counters()
	disk_read_count = str(disk[0])
	disk_write_count = str(disk[1])
	disk_read_time = str(disk[4])
	disk_write_time = str(disk[5])
	disk_busy_time = str(disk[6])

	network = psutil.net_io_counters(pernic=False, nowrap=True)
	network_bytes_sent = str(network[0])
	network_bytes_recv = str(network[1])
	network_packets_sent = str(network[2])
	network_packets_recv = str(network[3])
	network_errin = str(network[4])
	network_errout = str(network[5])
	network_dropin = str(network[6])
	network_dropout = str(network[7])


	body = cpu_percent + ", " + cpu_user_time + ", " + cpu_system_time + ", " + cpu_idle_time + ", " + cpu_iowait + ", " + cpu_irq + ", " + cpu_softirq + ", " + cpu_numbers_of_ctx_switches + ", " + cpu_numbers_of_interrupts
	body = body + ", " + cpu_numbers_of_soft_interrupts + ", " + cpu_load_runable_state + ", " + memory_percent + ", " + memory_active + ", " + memory_buffers + ", " + memory_cached + ", " + memory_shared + ", " + memory_swap_percent + ", " + memory_swap_sin + ", " + memory_swap_sout
	body = body + ", " + disk_usage_percent + ", " + disk_read_count + ", " + disk_write_count + ", " + disk_read_time + ", " + disk_write_time + ", " + disk_busy_time
	body = body + ", " + network_bytes_sent + ", " + network_bytes_recv + ", " + network_packets_sent + ", " + network_packets_recv + ", " + network_errin + ", " + network_errout + ", " + network_dropin + ", " + network_dropout +  "\n"

	print(str(counter)+":")
	print(body)


	f = open("dump.csv", "a")
	f.write(body)
	f.close()