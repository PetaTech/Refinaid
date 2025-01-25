import Link from 'next/link'
import { cva, type VariantProps } from 'class-variance-authority'


const buttonVariants = cva(
  [
    'ring-offset-background inline-flex items-center justify-center whitespace-nowrap rounded-lg text-sm font-medium transition-colors',
    'focus-visible:ring-ring focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2',
    'disabled:pointer-events-none disabled:opacity-50'
  ],
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline: 'border-input bg-background hover:bg-accent hover:text-accent-foreground border',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'text-primary underline-offset-4 hover:underline'
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 px-3',
        lg: 'h-11 px-8',
        icon: 'size-10'
      }
    },
    defaultVariants: {
      variant: 'default',
      size: 'default'
    }
  }
)


const Hero = () => {
  return (
    <div className='my-12 space-y-8'>
      <h1 className='text-3xl font-extrabold'>
        <span className='bg-gradient-to-r from-red-600 to-orange-500 bg-clip-text text-transparent'>
          Refinaid
        </span>{' - '}
        Bridging the Gap with AI For Everyone
      </h1>
      <p className='leading-6 text-muted-foreground'>
        An open-source learning platform, making AI accessible to everyone, no programming skills needed. Empowering all to explore the future of AI.
      </p>
      <div className='flex gap-4'>
        <Link href='#get-started' className={buttonVariants()}>
          Get started
        </Link>
        <Link
          href='https://github.com/1chooo/refinaid'
          className={buttonVariants({ variant: 'outline' })}
        >
          Source code
        </Link>
      </div>
    </div>
  )
}

export default Hero
