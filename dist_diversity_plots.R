library(ggplot2)
library(viridis)
library(ggthemes)
library(gridExtra)

setwd('~/3mee_talk/')

plot_base_size = 30
point_size = 3

data1 = data.frame(dist=0:100, diversity=sample(1750:2250, 101, replace=T)/1000, sel_type='no_sel')
str(data1)

data2 = data.frame(dist=0:100, diversity=data1$diversity*(data1$dist/100), sel_type='sel')

data3 = data.frame(dist=0:100, diversity=data1$diversity-(data1$diversity*(10/data1$dist)), sel_type='sel')

reg_data = rbind(data1, data3)
linked_data = rbind(data1, data2)

reg = ggplot(reg_data, aes(x=dist, y=diversity, colour=sel_type)) +
  geom_point(stat='identity', size=point_size) +
  theme_classic(base_size = plot_base_size) +
  ylim(0, 3) +
  scale_colour_manual(values=c(viridis(3)[1], NA)) +
  theme(legend.position = 'None', axis.title.x = element_blank(), axis.ticks = element_blank(),
        axis.text = element_blank())+
  ylab(expression(pi))

sel = ggplot(linked_data, aes(x=dist, y=diversity, colour=sel_type)) +
  geom_point(stat='identity', size=point_size) +
  theme_classic(base_size = plot_base_size) +
  ylim(0, 3) +
  scale_colour_manual(values=c(viridis(3)[1], NA)) +
  theme(legend.position = 'None', axis.title.x = element_blank(), axis.ticks = element_blank(),
        axis.text = element_blank()) +
  ylab('')

plot1 = grid.arrange(reg, sel, nrow=1)

reg2 = ggplot(reg_data, aes(x=dist, y=diversity, colour=sel_type)) +
  geom_point(stat='identity', size=point_size) +
  theme_classic(base_size = plot_base_size) +
  ylim(0, 3) +
  scale_colour_manual(values=viridis(3)) +
  theme(legend.position = 'None', axis.title.x = element_blank(), axis.ticks = element_blank(),
        axis.text = element_blank())+
  ylab(expression(pi))

sel2 = ggplot(linked_data, aes(x=dist, y=diversity, colour=sel_type)) +
  geom_point(stat='identity', size=point_size) +
  theme_classic(base_size = plot_base_size) +
  ylim(0, 3) +
  scale_colour_manual(values=viridis(3)) +
  theme(legend.position = 'None', axis.title.x = element_blank(), axis.ticks = element_blank(),
        axis.text = element_blank()) +
  ylab('')

plot2 = grid.arrange(reg2, sel2, nrow=1)

plot3 = grid.arrange(reg2, sel, nrow=1)

pdf('nosel_dist.pdf', width=12, height=3)

grid.arrange(reg, sel, nrow=1)

dev.off()

pdf('regsel_dist.pdf', width=12, height=3)

grid.arrange(reg2, sel, nrow=1)

dev.off()

pdf('allsel_dist.pdf', width=12, height=3)

grid.arrange(reg2, sel2, nrow=1)

dev.off()



